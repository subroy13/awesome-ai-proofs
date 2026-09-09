/* Shared, testable catalogue operations. No network calls or dependencies. */
(function (root) {
  'use strict';
  function counts(records, dimension) {
    const values = new Map();
    for (const record of records) for (const value of new Set(record[dimension])) values.set(value, (values.get(value) || 0) + 1);
    return [...values].sort(dimension === 'years' ? (a, b) => Number(a[0]) - Number(b[0]) : (a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  }
  function select(records, category, selection) {
    return records.filter(p => (!category || p.category === category) && (!selection || p[selection.dimension].includes(selection.value)));
  }
  function matches(row, filters) {
    const terms = filters.search.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    return terms.every(term => row.search.toLocaleLowerCase().includes(term))
      && (!filters.category || row.category === filters.category)
      && (!filters.subject || row.subjects.includes(filters.subject))
      && (!filters.model || row.models.includes(filters.model))
      && (!filters.evidence || row.evidence.includes(filters.evidence));
  }
  const api = {counts, select, matches};
  root.Catalogue = api;
  if (typeof module !== 'undefined') module.exports = api;
})(globalThis);
