export default function getListStudentIds(s) {
  if (!Array.isArray(s)) {
    return [];
  }
  return s.map(student => student.id);
}
