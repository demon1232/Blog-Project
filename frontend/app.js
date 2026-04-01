fetch("http://127.0.0.1:9000/api/blogs/")
  .then(res => res.json())
  .then(data => {
    let container = document.getElementById("blogs");

    data.forEach(blog => {
      let div = document.createElement("div");

      div.innerHTML = `
        <h3>${blog.title}</h3>
        <p>${blog.content}</p>
        <hr>
      `;

      container.appendChild(div);
    });
  });