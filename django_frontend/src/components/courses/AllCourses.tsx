import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Course } from "../../models/Course";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";

export const AllCourses = () => {
	const [loading, setLoading] = useState(false);
	const [courses, setCourses] = useState<Course[]>([]);

	useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/courses`)
			.then((response) => response.json())
			.then((data) => {
				setCourses(data);
				setLoading(false);
			});
	}, []);

	return (
		<Container>
			<h1>All courses</h1>

			{loading && <CircularProgress />}
			{!loading && courses.length === 0 && <p>No courses found</p>}
			{!loading && (
				<IconButton component={Link} sx={{ mr: 3 }} to={`/courses/add`}>
					<Tooltip title="Add a new course" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
			)}
			{!loading && courses.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">Name</TableCell>
								<TableCell align="right">Description</TableCell>
								<TableCell align="right">Teacher Name</TableCell>
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{courses.map((course, index) => (
								<TableRow key={course.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/courses/${course.id}/details`} title="View course details">
											{course.name}
										</Link>
									</TableCell>
									<TableCell align="right">{course.description}</TableCell>
									<TableCell align="right">{course.teacher?.name}</TableCell>
									<TableCell align="right">
										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/courses/${course.id}/details`}>
											<Tooltip title="View course details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/courses/${course.id}/edit`}>
											<EditIcon />
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/courses/${course.id}/delete`}>
											<DeleteForeverIcon sx={{ color: "red" }} />
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};
