void main(){

  // convert String to int ->
  String s = '10';
  int x = int.parse(s);
  print(x);
  print("The type of x is: $x".runtimeType);
  print("the type of s is: $s".runtimeType);

  // convert int to String ->
  int a = 6;
  String z = a.toString();
  print(z);
  print(a.runtimeType);
  print(z.runtimeType);

  //Uppercase and lower case ->
  String case1 = "test case is big :d";
  String case2 = "TEST CASE IS small :(";

  print(case1.toUpperCase());
  print(case2.toLowerCase());

  //check if a string is empty or not ->
  print('this is about case1:');
  print(case1.isEmpty);
  print('this is about case2:');
  print(case2.isNotEmpty);

  //check if a string contains a substring ->
  String name1 = 'Ali';
  print('this is about name1:');
  print(name1.contains("A"));

  //check the type of a variable ->
  dynamic case3 = 'Ahmed';
  case3 = 3;
  print('this is about case3:');
  print(case3 is String);
  print(case3 is int);
  print(case3);

  // Map test ->
  Map  <String, String> person = {
    "name": "Ali",
    "age" : "20",
    "address":"Helwan"
  };
  print(person);
//insert Map in List ->
  List <Map<String, String>> people = [];

  people.add(person);
  people.remove(person);

  //if and else ->
  if(people.contains(person)){
    print(people);
  }
  else{
    print("This is the second case 'Else' and we printing people...");
    people.add(person);
    print(people);

  }

  // for ->
  int i = 0;
  for(; i < 10; i++){
    if(i == 4) continue;
    print(i);
  }
  // for in ->
  List numbers = [0,1,2,3,4,5,6,7,8,9,10];
  for(int x in numbers ){
    if (x == 4) continue;
    print(x);
  }
  // forEach ->
  numbers.forEach((element) {
    if(element != 4)print(element);
  });

  // while ->
  while(i != 11){if(i != 4)print(i); i++;}

  // do...while ->
  do{
    if(i != 4)
    print(i);
    i++;
  }
  while(i < 11);
}

    

