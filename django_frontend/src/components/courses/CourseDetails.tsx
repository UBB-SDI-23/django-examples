import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Course } from "../../models/Course";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const CourseDetails = () => {
	const { courseId } = useParams();
	const [course, setCourse] = useState<Course>();

	useEffect(() => {
		const fetchCourse = async () => {
			// TODO: use axios instead of fetch
			// TODO: handle errors
			// TODO: handle loading state
			const response = await fetch(`${BACKEND_API_URL}/courses/${courseId}`);
			const course = await response.json();
			setCourse(course);
		};
		fetchCourse();
	}, [courseId]);

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/courses`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1>Course Details</h1>
					<p>Course Name: {course?.name}</p>
					<p>Course Description: {course?.description}</p>
					<p>Course Teacher Name: {course?.teacher?.name}</p>
					<p>Course students:</p>
					<ul>
						{course?.students?.map((student) => (
							<li key={student.id}>{student.name}</li>
						))}
					</ul>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/courses/${courseId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/courses/${courseId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};
