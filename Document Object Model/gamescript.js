var cells= document.querySelectorAll('td')
var restart = document.querySelector('#restart')

function clearBoard(){
  for (var i=0; i<cells.length; i++){
    cells[i].textContent = '';
}
}

function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X'
  }else if (this.textContent === 'X') {
    this.textContent = 'O'
  } else if (this.textContent === 'O') {
    this.textContent = ''
  }
}

for(cell of cells){
  cell.addEventListener('click', changeMarker)
}

restart.addEventListener('click', clearBoard);
