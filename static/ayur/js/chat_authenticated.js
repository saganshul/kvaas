var chatRef = new Firebase('https://bauth-chat.firebaseio.com'),
    target = document.getElementById("firechat-container"),
    chat = new FirechatUI(chatRef, target);

chatRef.onAuth(function(authData) {
  if (authData) {
    var userId = authData.uid,
        username = authData.auth.email.replace(/@.*/, '');

    chat.setUser(userId, username);
  } else {
      $.ajax({
          type:"GET",
          url: "/helper/generate_token/",
          success: function( data ) {
              var ref = new Firebase("https://bauth-chat.firebaseio.com");
              ref.authWithCustomToken(data, function(error, authData) {
                  if (error) {
                      console.log("Login Failed!", error);
                  } else {
                      console.log("Login Succeeded!", authData);
                  }
              });
          }
      });

}
});
function logout() {
  chatRef.unauth();
  console.log("Unauthenticated!")
  location.reload();
}
function togglechat() {
    $( "#firechat-container" ).slideToggle( "slow" );
}
