// document.getElementById("patient").onclick = function fun()
//     {
     
//      document.getElementById("reg").innerHTML ='<form method="POST" action="{% url "home" %}">'+
//      '{% csrf_token %} <div class="form-row">'+
//     '<div class="col"><input type="text" id="first" class="form-control" placeholder="First name"></div>'+
//     '<div class="col"><input type="text" id="last" class="form-control" placeholder="Last name"></div>'+
//   '</div><div class="form-row"><div class="col">'+
//       '<input type="email" class="form-control" name="email" placeholder="Email"></div><div class="col">'+
//     '<input type="password" class="form-control" name = "password" placeholder="Password"></div>'+
//   '</div><div class="form-row"><div class="col">'+
//   '<select id="" class="form-control"><option selected>Gender</option>'+
//         '<option>Male</option><option>Female</option><option>Others</option>'+
//       '</select></div><div class="col">'+
//       '<input type="text" id="bday" class="form-control datepicker" placeholder="Birth Day"></div></div>'+
//     '<input class="btn btn-primary btnn" type="submit" value="Register"></form>';

//      $('.datepicker').datepicker();
//     }  
// document.getElementById("doctor").onclick = function fun()
//     {
//     	   document.getElementById("reg").innerHTML ='<form><div class="form-row">'+
//     '<div class="col"><input type="text" id="first" class="form-control" placeholder="First name"></div>'+
//     '<div class="col"><input type="text" id="last" class="form-control" placeholder="Last name"></div>'+
//   '</div><div class="form-row"><div class="col">'+
//       '<input type="email" class="form-control" placeholder="Email"></div><div class="col">'+
//     '<input type="password" class="form-control" placeholder="Password"></div>'+
//   '</div><div class="form-row"><div class="col">'+
//   '<select id="" class="form-control"><option selected>Gender</option>'+
//         '<option>Male</option><option>Female</option><option>Others</option>'+
//       '</select></div><div class="col">'+
//       '<input type="text" id="bday" class="form-control datepicker" placeholder="Birth Day"></div></div>'+
//     '<input class="btn btn-primary btnn" type="submit" value="Register"></form>';

//      $('.datepicker').datepicker();
     
//      //validation code to see State field is mandatory.  
//     }  
// document.getElementById("hospital").onclick = function fun()
//     {
//      	document.getElementById('reg').innerHTML =  '<form><div class="form-row"><div class="col">'+
//       '<input type="text" id="hospitalName" class="form-control" placeholder="Hospital name"></div></div>'+
//   	   '<div class="form-row"><div class="col"><input type="text" id="hospitalReg" class="form-control" placeholder="Registration Number">'+
//     '</div><div class="col"><select id="" class="form-control"><option selected>Type</option><option>Government</option><option>Private</option>'+
//       '</select></div></div><div class="form-row"><div class="col"><input type="email" class="form-control" placeholder="Email">'+
//     '</div><div class="col"><input type="password" class="form-control" placeholder="Password"></div></div>'+
//     '<input class="btn btn-primary btnn" type="submit" value="Register"></form>'
//      //validation code to see State field is mandatory.  
//     }  


// $("#add_degree").click(function(){
//   $("#add_degrees").append('<div class="form-row"><div class="col"><input type="text" class="form-control" id="college" name="new_college" placeholder="Enter the College" value="">'+
//             '</div><div class="col"><input type="text" class="form-control" id="degree" name="new_degree" placeholder="Enter the Degree" value="">'+
//             '</div><div class="col"><button type="button" class="btn btn-danger"><a id="can_deg">Cancel</a></button></div></div><br>');
 
// });

// $("#add_spec").click(function(){
//   $("#add_speci").append('<br><div class="form-row">'+
//                '<div class="col"><input type="text" class="form-control" id="treatment" name="new_treatment" placeholder="Enter the Treatment" value="Add Your Specialization"></div>'+
//                '<div class="col"> <button type="button" class="btn btn-danger"><a id="can_spec">Cancel</a></button></div>'+
//             '</div>');

// });

//   $("#can_deg").click(function(){
//   $(this).parent().parent().parent().remove();
// });


//  $("#can_spec").click(function(){
//   $(this).parent().parent().parent().remove();
//   console.log("Hello");
// });

