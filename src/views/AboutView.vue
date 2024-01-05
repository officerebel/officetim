<template>
  <div>
      <h1 class="green">About</h1>
      <br>

      <p> I am {{ calculateAge }}  years old and have wife and two kids.</p>
  <p>My hobbies next to programming and building software are snowboard skateboard, dj and play the piano and make pizza.</p>
  <br>
  <p>My career path is broad but I was always interested in software and tech. Did you knew I launched coffee in one of the biggest supermarket chains? And starred in a tv show about coffee?</p>
  <p>That path lays long behind me and now I am focussed around my family my hobbies and work </p>
    <p>Skills:</p>
      <li>AWS architecture and infra building (sort of an solutions architect but not certified)</li>
      <li>Python, Django, Wagtail, Flask, Fastapi, DRF</li>
      <li>Vue.js, Vite, Axios</li>
      <li>Terraformer , Terraform Polumi</li>
      <li>Docker Postgresql, Msql, </li>
      <li>Senior technical (agile ,scrum) project lead</li>
      <br>
      <p>I've lived on planet earth for {{ calculateAge }} years and have worked on the web for {{ calculateExperience }} of them.</p>
<br>
</div>
</template>

<script>
export default {
  computed:{
    calculateAge: function() {
      let currentDate = new Date();
      let birthDate = new Date("1974/12/10");
      let difference = currentDate - birthDate;
      let age = Math.floor(difference/31557600000);
      return age
    },
    calculateExperience: function() {
      let currentDate = new Date();
      let startDate = new Date("2010/02/01");
      let difference = currentDate - startDate;
      let experience = Math.floor(difference/31557600000);
      return experience
    }
  }
}
</script>