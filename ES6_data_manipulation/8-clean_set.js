export default function cleanSet(set, startString) {
  const array = [];
  if (startString === '') {
    return '';
  }
  for (const ele of set) {
    if (ele.startsWith(startString)) {
      array.push(ele.slice(startString.length));
    }
  }
  return array.join('-');
}
