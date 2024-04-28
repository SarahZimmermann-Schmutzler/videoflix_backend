let myData = {
    'encoded_pk': ''
};

window.onload=async function(){
    try{
        let PatchRequest = await fetch(
            'account_activation/',
            {
                method: 'PATCH',
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(myData)
            }).then(function(response) {
                return response.json();
            }).then(function(data) {
                console.log("Data is ok", data);
            });
    } catch (e) {
        console.error('An error occured', e)
    }
}