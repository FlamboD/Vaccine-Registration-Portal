function hide()
{
    const second = $("#second");
    const main = $("#label-year");
    main.css("display","none");
    second.css("display","block");
}
function redirect()
{
    const choiceSelect =$("#choice :selected");
    const choice =$("#choice");
    const choiceWarning =$(".choice-warning")[0];
    if (choiceSelect.text()==="")
    {
        choiceWarning.innerHTML="This field must be selected";
        choiceWarning.css("color","red");
        choice.css("border-color","red");
    }
    else if(choiceSelect.text()==="No")
    {
        choiceWarning.innerHTML="Tap the box above to make a choice";
        alert("You must be years or older");
    }
}