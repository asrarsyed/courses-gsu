/*
starter code
*/

public class Lab02
{
    public static void main(String[] args)
    {
        Student students[] = new Student[2];
        int i;
        students[0] = new UndergraduateStudent(111, "Lambert");
        students[1] = new UndergraduateStudent(122, "Lembeck");
		System.out.println("\n\n\n\nUndergraduate Students:");
		
        for(i = 0; i < students.length; ++i) 
		{
			System.out.println("Student ID: " +
			                    students[i].getId() + ", Name: " +
			                    students[i].getLastName() + ", Tuition: " +
			                    students[i].getTuition() + " per year, " +
			                    "Student Class is: " + students[i].getClassification());
		}
		// NOTE: output for first UndergraduateStudent should be:
		// "Student ID: 111, Name: Lambert, Tuition: 4000 per year, Student Class is: Undergraduate"
		
		System.out.println("\n\n\nGraduate Students:");
		
		// REUSE the students[] array and create two GraduateStudent objects
		// Initialize with ID and lastname values
		// Print the two graduates with identical "for loop"
		// use very similar code as above...
		
		Student GradStudents[] = new Student[2];
        int j;
        GradStudents[0] = new GraduateStudent(133, "George");
        GradStudents[1] = new GraduateStudent(144, "Alexander");

        for (j = 0; j < GradStudents.length; ++j) {
            System.out.println("Student ID: " +
                    GradStudents[j].getId() + ", Name: " +
                    GradStudents[j].getLastName() + ", Tuition: " +
                    GradStudents[j].getTuition() + " per year, " +
                    "Student Class is: " + GradStudents[j].getClassification());
        }
		
		// System.out.println("\n\n\nProgrammer is: Dr. Johnson\n\n\n\n");
        System.out.println("\n\n\nProgrammer is: Asrar Syed\n\n\n\n");
    }
}
