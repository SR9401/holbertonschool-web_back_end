export default function getStudentIdsSum(s) {
 return s.reduce((sum, student) => sum + student.id, 0);
}