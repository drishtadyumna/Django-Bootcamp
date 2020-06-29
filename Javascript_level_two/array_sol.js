var command = null
var students = []
while (true){
  var command = prompt('Welcome! Enter one of the these commands: add, remove, display, or quit')
  if (command == 'add'){
    var stud = prompt('Enter name of student to be added')
    students.push(stud)
  }
  else if (command == 'remove'){
    var stud = prompt('Enter name of student to be remnoved')
    students.splice(students.indexOf(stud, 1))
  }
  else if (command == 'display'){
    console.log(students);
  }
  else if (command == 'quit'){
    alert('Thank you for visiting. Refresh the page to start again')
    break
  }
  else{
    alert('Command not recognised')
}
}
