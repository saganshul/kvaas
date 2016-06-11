var chatRef = new Firebase('https://bauth-chat.firebaseio.com'),
    target = document.getElementById("firechat-container"),
    chat = new FirechatUI(chatRef, target);

chatRef.onAuth(function(authData) {
  if (authData) {
    var userId = authData.uid,
        username = authData.auth.email.replace(/@.*/, '');

    chat.setUser(userId, username);
  } else {
      console.log("you need to authenticate to chat");

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
