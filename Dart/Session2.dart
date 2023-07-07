// void main(){
//
//   int min = 18;
//   List <Map<String, dynamic>> case1 = [];
//   case1.addAll({
//     {"Name": "Abdelrahman", "Age": 18},
//     {"Name": "Mostafa","Age": 23},
//     {"Name": "Ali","Age": 16},
//   });
//   case1.forEach((Map<String,dynamic> item){
//     if(item["Age"] >= min){
//       print("${item["Name"]} is accepted");
//     }
//     else{
//       print("${item["Name"]} is not accepted because he is ${item["Age"]} years old and the minimum age is $min");
//     }
//   });
//
// }

// int sum({int? x = 0, int? y = 0, int? z = 0}) {
//   return x! + y! + z!;
// }
//
// void main(){
//
// print(sum(x: 5 ,y: 2));
//
// }

// int sum(int x ,int y,[int z = 0 ]) {
//   return x + y + z;
// }
//
// void main(){
//
// print(sum(2,3));
//
// }


// int sum(int x1,int x2) => x1+x2;
// void hello() => print("hello");
// void x() => print("Hello World!");


//
// class Car{
//   late String modelYear;
//   late String type;
//   late String color;
//   void start(){
//     print("The color of the ${type} is ${color}");
//   }
// }
// void main(){
//   Car bmw=Car();
//
//   bmw.type="MER";
//   bmw.color="Black";
//   bmw.modelYear="2020";
//
//   bmw.start();
//
// }


// class person {
//   late String name;
//   late String age;
//   late String home;
//   late String faculty;
//   late String level;
//
//   void info(){
//     print("Student name is ${name} he is ${age} years old and he is living in ${home}.");
//   }
//   void moreinfo(){
//     print("He is a student at the faculty of ${faculty} and he is level ${level}.");
//   }
// }
//
// void main(){
//   person info = person();
//
//   info.name = "Abdelrahman";
//   info.home = "Helwan";
//   info.age = "18";
//   info.faculty = "BIS";
//   info.level = "1";
//
//   info.info();
//   info.moreinfo();
// }


//
// class Employee
// {
//
// String name = "";
// int age = 0;
// double salary = 0.0;
//
// Employee({String? name, int? age, double? salary}) {
//   this.name = name!;
//   this.age = age!;
//   this.salary = salary!;
// // note that you can remove ? , !  and add required before String, int and double.
//
// }
//
//   void printData(){
//     print("${name} is ${age} years old and his salary = ${salary}");
//   }
// }
// void main (){
//   Employee one=Employee (name:"ahmed",age:20,salary:3500.5);
//   one.printData();
// // now the output should be like this => ahmed is 20 years old and his salary = 3500.5
// }


class customer {
  String name = "";
  String serves = "";
  dynamic date = 0;
  String feedback = "";

  customer(
      {required String name, required String serves, required dynamic date, String? feedback}) {
    this.name = name;
    this.serves = serves;
    this.date = date;
    this.feedback = feedback!;
  }

  void output(){
    print("The customer name is ${name} the serves he needs is ${serves} on date ${date} and the feedback was ${feedback}. ");
  }
}

void main(){
  customer info = customer(
      name: "Khalid",
      serves: "\"failed internet connection\",\n",
      date: "Thu, 11 May", feedback: "Problem solved successfully");
  info.output();
}
