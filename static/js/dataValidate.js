function hide()
{
    $("#label-gender").css("display","none");
    
}
function enableButton()
{
    const submitButton = $("#next");
    let checkbox =$("#flexCheckDefault").is(":checked");
    if (submitButton.attr("disabled") && checkbox)
    {
        submitButton.removeAttr("disabled");
    }
    else
    {
        submitButton.attr("disabled","true");
    }
}
function date()
{
    const calendar = $("#calendar");
    $(document).ready(function(){
        calendar.datepicker();
    })
}
function validate(checksum)
{
    const id = $("#IDNumber");
    const confID = $("#confIDNumber");
    const cidLabel = $("#cid-label");
    const idLabel = $("#id-label");
    const validLabel = $("#valid-id");
    let DOB = $("#dob");

    if (checksum)
    {   
        validLabel.css("display","none")
        confID.css("display","block");
        DOB.val(getDOB(id.val()));
        id.css("border-color","#9b9b9b");
        idLabel.css("color","#9b9b9b");

        
    }
    else
    {
        validLabel.css("display","block");
        idLabel.css("color","red");
        confID.css("display","none");
        id.css("border-color","red");
    }
}

function isValidDOB(IDNum)
{
    let year;
    let day;
    let month;
    if (!(isNaN(IDNum)) && IDNum.length>=6)
    {
        year = parseInt(IDNum.substr(0,2),10);
        month = parseInt(IDNum.substr(2,2),10);
        day = parseInt(IDNum.substr(4,2),10);
        if (((year>=21 && year<=99) || (year>=0 && year<=3)) && (month>=1 && month<=12) && (day>=1 && day<=31))
        {
            return true;
        }
        else
        {
            return false
        }
    }
}
function isValidGender(IDNum)
{
    let gender;
    let citizenship;
    let digit;
    if (!(isNaN(IDNum)) && IDNum.length>=12)
    {
        gender = parseInt(IDNum.substr(6,4),10);
        citizenship = parseInt(IDNum.substr(10,1),10);
        digit = parseInt(IDNum.substr(11,1),10);
        if ((gender>=0 && gender<9999) && (citizenship===0 || citizenship===1) && digit===8)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
function getDOB(IDNum)
{
    let Syear;
    let year
    let Sday;
    let day
    let Smonth;
    let month;
    let DOB;
    if (isValidDOB(IDNum))
    {
        year = parseInt(IDNum.substr(0,2),10);
        if (year>=21 && year<=99)
        {
            Syear = "19"+year.toString();
        }
        else
        {
            Syear = "200"+year.toString();
        }
        month = parseInt(IDNum.substr(2,2),10);
        if (month<10)
        {
            Smonth ="0"+month.toString();
        }
        else
        { 
            Smonth = month.toString();
        }
        day = parseInt(IDNum.substr(4,2),10);
        if (day<10)
        {
            Sday ="0"+day.toString();
        }
        else
        { 
            Sday = day.toString();
        }
        DOB = Syear+"/"+Smonth+"/"+Sday;   
    }
    return DOB;
}

