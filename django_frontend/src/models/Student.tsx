import { Course } from "./Course";

export interface Student {
	id: number;
	name: string;
	email: string;
	address?: string;
	age: number;
	courses: Course[];
}
