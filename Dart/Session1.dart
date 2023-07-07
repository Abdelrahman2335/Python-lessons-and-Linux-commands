// void main(){
  // String name = "Abdelrahman";
  // String age = "18";
  // double age2 = 18.55;
  // var myAge = 18;
  //
  // // to convert string to int ->
  // print("The name is $name");
  // print(age2);
  // int ageNum = int.parse(age);
  // print(age2.toStringAsFixed(1));
  // print(myAge.runtimeType);
  //
  // print("The age is $ageNum");
  //
  // String test = "test case is big :d";
  // print(test.toUpperCase());
  // print(name.isNotEmpty);
  // print(name.isEmpty);
  // print(name.contains('rahman')); // note that contains not for int but you can use it if you change the type.
  //
  // bool isCharge = true;

// import 'dart:io';

// import 'dart:html';

// import 'dart:io';


void main() {

// // Input and Output: you have to use import 'dart:io';
//   print("Enter your name:");
//   String name = stdin.readLineSync()!;
//   int age = int.parse(stdin.readLineSync()!);
//   print(name);
//   print(age);
//   age is int; // this small error shown cuz the result always true

 //  print("Enter your name:");
 //  dynamic name1 = (stdin.readLineSync()!);
 // bool x = name1 == int;
 //  if (x = true){
 //    print("Please Enter String only");
 //
 //  }
//   print("Enter your name:");
//   var name2 = (stdin.readLineSync()!);
//   print("Enter your age:");
//   int age1 = int.parse(stdin.readLineSync()!);
//   print("Enter your age:");
//   int age2 = int.parse(stdin.readLineSync()!);
//
// // if, else if and else:
//   if(name1 is int ){
//     print("please Enter string only");
//   }
//   if(name2 is int){
//     print("please enter string only");
//   }
//   if(age1 < age2 ){
//     print("$name2 is older than $name1");
//   }
//   else if(age1 == age2){
//     print("$name1 and $name2 is the same age :D");
//   }
//   else{
//     print("$name1 is older than $name2");
//   }

// // switch case:
// print("Enter the grade:");
//   String grade = stdin.readLineSync()!;
//   switch(grade){
//     case 'A': print("Excellent");
//     break;
//     case 'B': print("Very Good");
//     break;
//     case 'C': print("Good");
//     break;
//     case 'F': print("Failed");
//     break;
//     default:
//       print("Error");
//   }print("Please enter your age:");
// //   int age = int.parse(stdin.readLineSync()!);
// //   String isAccepted = age >= 16?"Accepted": age < 16?"Not Accepted":"Error";
// //   print(isAccepted);
//

// dynamic and var:
//   dynamic age = 15;
//   age = "15";
//   print(age);
//   var value = '5'; // var is like dynamic but var you can't change it like dynamic
//   // value = 5; // this error shown CUZ you can't change the type when you are using 'var'
//   print(value);

// LIst:
  List studentNames = ["Mohamed","Nagi","Abdelrahman","Sayed"];
  List <String> studentNames2 = ["Mohamed", "Nagi", "Abdelrahman", "Sayed"];
  print(studentNames);

  studentNames.add("Hagar");

  studentNames.remove("Sayed");

  studentNames.removeAt(0);

  int length = studentNames2.length;

  print(length);

  print(studentNames);

  studentNames[0] = "yasser";
  
  print(studentNames);

// Set:
//   Set <int> mySet = {1,2,3,4};
//   Set <String> EmptySet = {};
//   // adding some elements...
//   EmptySet.add("Ali");
//   EmptySet.add("Ahmed");
//   EmptySet.add("Khalid");
//
//   print(mySet);
//   print(EmptySet);
//   // to remove elements from a Set...
//   mySet.remove(4);
//   print(mySet);
//   print(EmptySet.contains("Ali"));
//   print(EmptySet.contains("Alia"));
//   // What is union ?
//   Set <int> set1 = {1, 2, 3};
//   Set <int> set2 = {2, 3, 4};
//   Set <int> set3 = set1.union(set2);
//   print(set3);

// Note that Sets are typically faster than Lists for checking whether an element is in the collection or not,
// as they use hash codes to store and look up elements.

// Map:
//   Map <String, int> myMap = {"apple": 1, "banana": 2, "cherry": 3};
//   Map <String, int> EmptyMap = {};
//   // adding some elements...
//   EmptyMap['Apple'] = 1;
//   EmptyMap['cherry'] = 2;
//   EmptyMap['banana'] = 3;
//
// // convert Map to List:
//   List <String> x = myMap.keys.toList();
//   List <int> y = myMap.values.toList();
//   print("Lovely output $x and $y.");
//
// for (var element in myMap.entries) {
//   print('${element.value}: ${element.key}');
// }

// for loop:
  // int counter = 0;
  // for(;counter < 10;)
  // {
  //   print("Hello world!");
  //   counter++;
  // }

// for each:
  // Map:
  // myMap.forEach((String key,int value)
  // {
  //   print("${key}'s number = ${value}");
  // });

// for in:
  // for (String x in studentNames2){
  //   print(x);
  // }

//while:
//   int x = 0;
//   while(x < 5){
//     print("This is while loop I will stop after 5 :D");
//     x++;
// }

  // bool Connected = false;
  // while(Connected){
  //   print("Notification");
  // }

// do..while:
//   do{
//     print("Notification");
//   }while(Connected);

//Continue:
//   for(int x = 0; x < 10; x++){
//     if( x == 5){
//       continue;
//     }
//     print(x);
//   }

}
