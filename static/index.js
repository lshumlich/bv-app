console.log('Hello from Static');
window.onload = (event) => {
    console.log('page is fully loaded');
    console.log('idCities', idCities);
    if(idCities) {
        // console.log('added event listener');
        idCities.addEventListener('change', (e) => {
            const selected = e.target.value;
            // idSelectedCity1.innerText = selected;
            // idSelectedCity2.innerText = selected;
            idImage.src = `/static/images/${selected}.jpeg`;
        });
    }
};