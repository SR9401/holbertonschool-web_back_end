export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      const resp = {
        status: 200,
        body: 'Succes',
      };
      resolve(resp);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
