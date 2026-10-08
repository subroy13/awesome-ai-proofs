'use strict';
const form = document.querySelector('#filters');
if (form) {
  const tbody = document.querySelector('tbody');
  const rows = [...tbody.rows];
  const fields = Object.fromEntries(['search', 'category', 'subject', 'model', 'evidence', 'sort'].map(id => [id, document.getElementById(id)]));
  const data = new Map(rows.map(row => [row, {...row.dataset, subjects: JSON.parse(row.dataset.subjects), models: JSON.parse(row.dataset.models), evidence: row.dataset.evidence.split(' ')}]));
  function applyFilters() {
    const filters = Object.fromEntries(Object.entries(fields).map(([id, field]) => [id, field.value]));
    const ordered = [...rows];
    if (filters.sort === 'title') {
      ordered.sort((a, b) => a.querySelector('.problem-title').textContent.localeCompare(b.querySelector('.problem-title').textContent));
    } else if (filters.sort === 'oldest') {
      ordered.sort((a, b) => a.dataset.date.localeCompare(b.dataset.date) || a.querySelector('.problem-title').textContent.localeCompare(b.querySelector('.problem-title').textContent));
    } else if (filters.sort === 'catalogue') {
      ordered.sort((a, b) => ['Research', 'Competitions', 'Historical'].indexOf(a.dataset.category) - ['Research', 'Competitions', 'Historical'].indexOf(b.dataset.category) || a.querySelector('.problem-title').textContent.localeCompare(b.querySelector('.problem-title').textContent));
    } else {
      ordered.sort((a, b) => b.dataset.date.localeCompare(a.dataset.date) || a.querySelector('.problem-title').textContent.localeCompare(b.querySelector('.problem-title').textContent));
    }
    let count = 0;
    for (const row of ordered) {
      row.hidden = !Catalogue.matches(data.get(row), filters);
      if (!row.hidden) count++;
      tbody.append(row);
    }
    document.getElementById('result-count').textContent = `${count} of ${rows.length} records`;
    document.getElementById('empty').hidden = count !== 0;
  }
  form.hidden = false;
  form.addEventListener('input', applyFilters);
  form.addEventListener('change', applyFilters);
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('reset', () => setTimeout(applyFilters, 0));
}
const payload = document.getElementById('chart-data');
if (payload) {
  const records = JSON.parse(payload.textContent);
  const category = document.getElementById('viz-category');
  const listRows = [...document.querySelectorAll('[data-record]')];
  let selection = null;
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
  function showRecords() {
    const selected = Catalogue.select(records, category.value, selection);
    const ids = new Set(selected.map(p => p.id));
    for (const row of listRows) row.hidden = !ids.has(row.dataset.record);
    document.getElementById('selection-title').textContent = selection ? selection.value : (category.value || 'All records');
    document.getElementById('selection-count').textContent = `${selected.length} records`;
    for (const bar of document.querySelectorAll('.chart-bar')) {
      const active = Boolean(selection && bar.dataset.dimension === selection.dimension && bar.dataset.value === selection.value);
      bar.setAttribute('aria-pressed', String(active));
      bar.classList.toggle('selected', active);
    }
  }
  function draw() {
    const subset = Catalogue.select(records, category.value, null);
    document.getElementById('viz-count').textContent = `${subset.length} records`;
    for (const dimension of ['years', 'evidence', 'models', 'subjects']) {
      const values = Catalogue.counts(subset, dimension);
      const maximum = Math.max(1, ...values.map(([, count]) => count));
      document.getElementById(`chart-${dimension}`).innerHTML = values.map(([value, count]) => `<button type="button" class="chart-bar ${dimension === 'evidence' ? escape(value) : ''}" data-dimension="${dimension}" data-value="${escape(value)}" aria-pressed="false" aria-label="${escape(value)}: ${count} records"><span class="bar-label">${escape(value)}</span><span class="bar-track"><span style="width:${count / maximum * 100}%"></span></span><strong>${count}</strong></button>`).join('') || '<p>No records.</p>';
    }
    showRecords();
  }
  document.querySelector('.chart-grid').addEventListener('click', event => {
    const bar = event.target.closest('.chart-bar');
    if (!bar) return;
    event.preventDefault();
    const next = {dimension: bar.dataset.dimension, value: bar.dataset.value};
    selection = selection && selection.dimension === next.dimension && selection.value === next.value ? null : next;
    showRecords();
  });
  category.addEventListener('change', () => {selection = null; draw();});
  document.getElementById('viz-reset').addEventListener('click', () => {category.value = ''; selection = null; draw();});
  draw();
}
// Open linked explanatory sections when navigating directly to their anchor.
function revealSection() {
  if (!location.hash) return;
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target && target.tagName === 'DETAILS') target.open = true;
}
revealSection();
window.addEventListener('hashchange', revealSection);
