import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Course } from "../../models/Course";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";

export const CourseAdd = () => {
	const navigate = useNavigate();

	const [course, setCourse] = useState<Course>({
		name: "",
		description: "",
		teacher_id: 1, // TODO: also read the teacher_id from the form (NOT from the user!)
	});

	const addCourse = async (event: { preventDefault: () => void }) => {
		event.preventDefault();
		try {
			await axios.post(`${BACKEND_API_URL}/courses/`, course);
			navigate("/courses");
		} catch (error) {
			console.log(error);
		}
	};

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/courses`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<form onSubmit={addCourse}>
						<TextField
							id="name"
							label="Name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setCourse({ ...course, name: event.target.value })}
						/>
						<TextField
							id="description"
							label="Description"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setCourse({ ...course, description: event.target.value })}
						/>

						<Button type="submit">Add Course</Button>
					</form>
				</CardContent>
				<CardActions></CardActions>
			</Card>
		</Container>
	);
};
