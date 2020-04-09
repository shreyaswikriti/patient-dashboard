document.getElementById("patient").onclick = function fun()
    {
     
     document.getElementById("reg").innerHTML ='<form><div class="form-row">'+
    '<div class="col"><input type="text" id="first" class="form-control" placeholder="First name"></div>'+
    '<div class="col"><input type="text" id="last" class="form-control" placeholder="Last name"></div>'+
  '</div><div class="form-row"><div class="col">'+
      '<input type="email" class="form-control" placeholder="Email"></div><div class="col">'+
    '<input type="password" class="form-control" placeholder="Password"></div>'+
  '</div><div class="form-row"><div class="col">'+
  '<select id="" class="form-control"><option selected>Gender</option>'+
        '<option>Male</option><option>Female</option><option>Others</option>'+
      '</select></div><div class="col">'+
      '<input type="text" id="bday" class="form-control datepicker" placeholder="Birth Day"></div></div>'+
    '<input class="btn btn-primary btnn" type="submit" value="Register"></form>';

     $('.datepicker').datepicker();
    }  
document.getElementById("doctor").onclick = function fun()
    {
    	   document.getElementById("reg").innerHTML ='<form><div class="form-row">'+
    '<div class="col"><input type="text" id="first" class="form-control" placeholder="First name"></div>'+
    '<div class="col"><input type="text" id="last" class="form-control" placeholder="Last name"></div>'+
  '</div><div class="form-row"><div class="col">'+
      '<input type="email" class="form-control" placeholder="Email"></div><div class="col">'+
    '<input type="password" class="form-control" placeholder="Password"></div>'+
  '</div><div class="form-row"><div class="col">'+
  '<select id="" class="form-control"><option selected>Gender</option>'+
        '<option>Male</option><option>Female</option><option>Others</option>'+
      '</select></div><div class="col">'+
      '<input type="text" id="bday" class="form-control datepicker" placeholder="Birth Day"></div></div>'+
    '<input class="btn btn-primary btnn" type="submit" value="Register"></form>';

     $('.datepicker').datepicker();
     
     //validation code to see State field is mandatory.  
    }  
document.getElementById("hospital").onclick = function fun()
    {
     	document.getElementById('reg').innerHTML =  '<form><div class="form-row"><div class="col">'+
      '<input type="text" id="hospitalName" class="form-control" placeholder="Hospital name"></div></div>'+
  	   '<div class="form-row"><div class="col"><input type="text" id="hospitalReg" class="form-control" placeholder="Registration Number">'+
    '</div><div class="col"><select id="" class="form-control"><option selected>Type</option><option>Government</option><option>Private</option>'+
      '</select></div></div><div class="form-row"><div class="col"><input type="email" class="form-control" placeholder="Email">'+
    '</div><div class="col"><input type="password" class="form-control" placeholder="Password"></div></div>'+
    '<input class="btn btn-primary btnn" type="submit" value="Register"></form>'
     //validation code to see State field is mandatory.  
    }  
