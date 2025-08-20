export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students) || !students.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of string');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(nName) {
    if (typeof nName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = nName;
  }

  set length(nLength) {
    if (typeof nLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = nLength;
  }

  set students(nstudents) {
    if (!Array.isArray(nstudents) || !nstudents.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    this._students = nstudents;
  }
}
