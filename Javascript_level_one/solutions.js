var fname = prompt("Welcome. Please enter your first name (all letters lowercase)")
var lname = prompt("Now enter your last name )all letter lowercase)")
var age = prompt("How old are you (in years)?")
var height = prompt("How tall are you (in cm)?")
var pname = prompt("What is your pet name (al letters lowercase)?")
var lindex = pname.length

if (fname[0]==lname[0] && 20<age<30 && height>=170 && pname[lindex-1]=="y"){
  console.log("Conratulations comrade. You have passed the test")
}

else{
  console.log("Sorry. Nothing to see here");
}
