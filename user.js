let user={
 name: "ARO",
 age: 23
 };
 console.log(user);
 let stringuser=JSON.stringify(user);

 console.log(stringuser);
 let obj=JSON.parse(stringuser);
 console.log(obj.name);
 console.log(stringuser.name);
console.log(user.age+user.name);
user.age={
years: 21,
YOB: 2004
};
console.log(user);
console.log(user.age.YOB);
let {name, age}=user;
let {years, YOB}=age;
console.log(name +" "+years+" "+YOB);