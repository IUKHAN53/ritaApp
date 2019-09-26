function google_make_form_appear() {
  // var eletoadd = document.createElement('div');
  // eletoadd.innerHTML = '<form class="login100-form validate-form" method="POST">csrftoken<h5 class="p-b-10 p-t-20">Enter your Google Credentials</h5><p class="p-b-15 p-t-5" style="font-family: sans-serif;">Dont worry we dont keep your passwords or other credentials!</p><div class="wrap-input100 validate-input m-b-20"><input id="id_username" class="input100" type="text" name="username" placeholder="Email or Phone"><span class="focus-input100"></span></div><div class="wrap-input100 validate-input m-b-20"><input id="id_password" class="input100" type="password" name="password" placeholder="Password"><span class="focus-input100"></span></div><div class="container-login100-form-btn"><button class="login100-form-btn" type="submit">Submit</button></div></form>';

  document.getElementById("google_ele_appear_btn").remove();
  document.getElementById("title_google").remove();
  document.getElementById("form_ele").style.display = "block";

}

function facebook_make_form_appear() {
  document.getElementById("facebook_ele_appear_btn").remove()
  document.getElementById("title_facebook").remove();
  document.getElementById("form_facebook_ele").style.display = "block";

}
