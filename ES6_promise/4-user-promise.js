export default function signUpUser(firstName, lastName) {
	return new Promise((resolve, reject) => {
		const res = {
  			firstName: `${firstName}`,
  			lastName: `${lastName}`,
		}
		resolve(res)
	})
}