<template>
  <v-app>
    <Navbar />
    <v-main class="main">
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
export default {
  name: "DefaultLayout",
  components: {
    Navbar,
  },
  data() {
    return {
      clipped: false,
    };
  },
};
</script>
<style>
/* display cards */
.header_ {
  display: flex;
  justify-content: space-between;
}
.subtitle {
  display: flex;
  gap: 0.8rem;
}
ul {
  display: flex;
  flex-direction: column;
  gap: 18px;
  list-style: none;
}
h1,
p {
  color: #021c36;
}

/**/
.cardTitle {
  background-color: #1a3c40;
}
.theme--dark.v-application {
  background: whitesmoke;
  color: #cfd9e4;
}
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  background: #f4f4f4;
}
a {
  color: #666;
  text-decoration: none;
}
</style>
