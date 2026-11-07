fetch("http://127.0.0.1:5000/receive", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    name: "Mulax",
  })
})
  .then(res=> res.json())
  .then(data => {
    console.log(data);
  })