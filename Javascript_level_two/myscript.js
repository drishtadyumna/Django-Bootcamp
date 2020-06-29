var v = "global v"
var stuff ="global stuff"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func"
  console.log(stuff);
}

fun();

console.log(stuff);
