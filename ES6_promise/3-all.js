import { createUser } from "./utils";
import { uploadPhoto } from "./utils";

export default async function handleProfileSignup() {
	try {
		const [photoResult, userResult] = await Promise.all([uploadPhoto(), createUser()]);
    const firstName = userResult.firstName;
    const lastName = userResult.lastName;
	const body = photoResult.body;
		
	console.log(`${body} ${firstName} ${lastName}`);
	
	} catch (error) {
		console.log('Signup system offline');
	}
}
