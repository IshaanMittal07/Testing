/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test.inheritance;

/**
 *
 * @author ishmi
 */
public class TestInheritance {

    static class Person {

        public String firstName;
        public String lastName;
        public int age;
        private String siNumber;
        private String address;

        Person(String firstName, String lastName, int age, String siNumber, String address) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.siNumber = siNumber;
            this.address = address;

        }

        public String getAddress() {

            return this.address;
        }

        public void setAddress(String address) {
            if (address.isEmpty()) {
                return;
            }
            this.address = address;
        }

        @Override
        public String toString() {
            return "First name: \"" + this.firstName + "\", "
                    + "Last name: \"" + this.lastName + "\", "
                    + "Age: \"" + this.age + "\"";
        }

        @Override
        public boolean equals(Object obj) {

            if (this == obj) {
                return true;
            }
            if (obj == null || obj.getClass() != this.getClass()) {
                return false;
            }

            Person person = (Person) obj;

            return (person.firstName.equals(this.firstName)
                    && person.lastName.equals(this.lastName)
                    && person.siNumber.equals(this.siNumber));
        }

        class Student extends Person {

            int studentid;
            String grade;

            Student(String firstName, String lastName, int age, String siNumber, String address, int studentId, String grade) {
                super(firstName, lastName, age, siNumber, address);
                this.grade = grade;

            }

            @Override
            public String toString() {
                return "First Name: \"" + this.firstName + "\", " + 
                "Last Name: \"" + this.lastName + "\", " + 
                "Student ID: \"" + this.studentid + "\"" + 
                "Grade: \"" + this.grade + "\"";
                        

            }
        }
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Person student = new Person("some", "student", 14, "hi", "Your old address: 2263 Marine Drive");
        Person student2 = new Person("some", "student", 14, "hi", "Your old address: 2263 Marine Drive");

        System.out.println(student.equals(student2));
    }

}
