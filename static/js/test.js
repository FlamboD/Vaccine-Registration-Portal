function validate() {
    let input = document.getElementById("sa-id");
    let row = document.getElementById("sa-id-row");

    if (input.value.length === 13 && luhn(input.value))
        row.classList.remove("invalid")
    else
        row.classList.add("invalid");
} validate();

function luhn(number) {
    let total = 0;
    for(let i = 0; i < number.length; i++) {
        let _ = parseInt(number[i]) * (i % 2 + 1)
        if (_ > 9) _ = parseInt(_.toString()[0]) + parseInt(_.toString()[1])
        total += _;
    }
    return !(total % 10);
}