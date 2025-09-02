const fs = require('fs');

function countStudents(db) {
  let c;
  try {
    c = fs.readFileSync(db, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
  const l = c.split('\n').filter((line) => line.trim() !== '');
  const s = l.slice(1);
  console.log(`Number of students: ${s.length}`);
  const work = {};

  s.forEach((l) => {
    const p = l.split(',');
    const fn = p[0];
    const wk = p[3];
    if (!work[wk]) {
      work[wk] = [];
    }
    work[wk].push(fn);
  });
  Object.keys(work).forEach((wk) => {
    const l = work[wk].join(', ');
    console.log(`Number of students in ${wk}: ${work[wk].length}. List: ${l}`);
  });
}

module.exports = countStudents;
