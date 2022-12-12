// Get the modal
/* var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
 */


function filterItems(){
  let input, filter, ul, li, txtValue;
  input = document.getElementById("filterSearch");
  filter = input.value.toUpperCase();
  ul = document.getElementById("especialidadesRow");
  li = ul.getElementsByClassName("especialidad-item");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}

function clickedItem(especialidad_id, especialidad_descripcion){
  //let item = document.getElementsByClassName("especialidad-item");

  const data = { id: especialidad_id };
  const url = document.getElementById('url-med').innerHTML.replace(/"|"/g,'');
  const div = document.getElementById('medicos_row');

  const csrftoken = getCookie('csrftoken');
  fetch(url, {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
      body: JSON.stringify(data),
    })
  .then((response) => response.json())
  .then((data) => {
    //console.log('Success:', data);
    let html = '';
    data.forEach(element => {
      html += '<div class="col-lg-6">'
      +'<div class="member d-flex align-items-start">'
      +'<div class="pic"><img src="/static/assets/img/doctors/doctors-1.jpg" class="img-fluid" alt=""></div>'
      +'<div class="member-info">'
      +`<h4>${element.nombres} ${element.apellidos}</h4>`
      +`<span>${especialidad_descripcion}</span>`
      +'<p>Explicabo voluptatem mollitia et repellat qui dolorum quasi</p>'
      +`<a href="/agendar/medico/${element.id}">Agendar Hora</a>`
      +'<div class="social">'
      +'<a href=""><i class="ri-twitter-fill"></i></a>'
      +'<a href=""><i class="ri-facebook-fill"></i></a>'
      +'<a href=""><i class="ri-instagram-fill"></i></a>'
      +'<a href=""> <i class="ri-linkedin-box-fill"></i> </a>'
      +'</div>'
      +'</div>'
      +'</div>'
      +'</div>';
    });
    div.innerHTML = html;
  })
  .catch((error) => {
    console.error('Error:', error);
  });

  
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}