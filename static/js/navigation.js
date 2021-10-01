function clicked(index)
{
    const dropdown = $("#dropdownMenuButton");
    const links = $(".dropdown-item");
    dropdown.val(links[index].innerHTML)
}
function cont_secondPage()
{
    const dropdown = $("#dropdownMenuButton");
    const navigateLink = $("#navigateID");
    if (dropdown.val()!=="Yes")
    {
        navigateLink.href = "#";
        alert("You need to be 18 years or older");
    }
    

}