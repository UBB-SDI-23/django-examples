import { Student } from "./Student";
import { Teacher } from "./Teacher";

export interface Course {
	id?: number;
	name: string;
	description: string;
	teacher_id?: number;
	teacher?: Teacher;
	students?: Student[];
}
