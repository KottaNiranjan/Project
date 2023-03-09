app.controller('ctrl', function ($window, $scope) {

    $scope.initData = [
        {
            name: "Niranjan",
            pass: "Niranjan@123",  
        },
        {
            name: "Jane",
            pass: "Doe",
        },
        {
            name: "John",
            pass: "Smith",
        }
    ];
    console.log(name,pass)
    $window.localStorage.setItem('initData', JSON.stringify($scope.initData));
    $scope.retrievedData = JSON.parse($window.localStorage.getItem('initData'));
    $scope.sortedType = 'name';
    $scope.sortedReverse = false;
    //Remove Rows and Update localStorage Key Values
    $scope.removeRow = function(row) {
        $scope.retrievedData.splice(row, 1);
        $scope.initData.splice(row, 1);
        $window.localStorage.setItem('initData', JSON.stringify($scope.initData));
    }
});

function re(){
var dict={}
var n=document.getElementById("name").value
var p=document.getElementById("pass").value
console.log(n,p)
dict[n]=p 
for (var i in dict){
    console.log(i,"=>",dict[i])
}
}


