function validate()
{
    const id = $("#IDNumber");
    const confID = $("#confIDNumber");
    const IDlabel = $("#id-label");
    let DOB = $("#dob");

    if ((validateChecksum(id.val()) || isValidDOB(id.val()) || isValidGender(id.val())))
    {   
        confID.css("display","block");
        DOB.val(getDOB(id.val()));
        
    }
    else
    {
        confID.css("display","none");
        id.css("border-color","red");
    }
}
function validateChecksum(IDNum)
{
    let sum=0;
    let miniSum=0;
    let product;
    let currentDigit;
    let checksum=null;
    if (!(isNaN(IDNum)) && IDNum.length===13)
    {
        for (let i=0;i<12;i++)
        {
            currentDigit = parseInt(IDNum.substr(i,1),10);
            if (!(i%2===0))
            {
                product = currentDigit*2;
                if (product>9)
                {
                    miniSum = parseInt(product.toString()[0],10) +parseInt(product.toString()[1],10)
                    sum +=miniSum;
                }
                else
                {
                    sum += product; 
                }
            }
            else
            {
                sum += currentDigit;
            }
        }
    }
    checksum = 10 - (sum%10);
    if (checksum>9)
    {
        checksum = 0;
    }
    if (checksum === parseInt(IDNum[12],10))
    {
        return true;
    }
    else
    {
        return false;
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
