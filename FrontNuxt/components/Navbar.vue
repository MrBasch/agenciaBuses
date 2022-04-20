<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div id="header">
      <div class="title_navbar" href="/">Reisebüro</div>
      <v-spacer />
      <div class="navbar-start">
        <nuxt-link to="/buses">Buses</nuxt-link>
        <nuxt-link to="/route">Route</nuxt-link>
        <nuxt-link to="/travel">Travel</nuxt-link>
        <nuxt-link to="/passenger">Passenger</nuxt-link>
        <nuxt-link to="/driver">Driver</nuxt-link>
        <nuxt-link to="/city">City</nuxt-link>
        <nuxt-link to="/station">Station</nuxt-link>
        <nuxt-link to="/place">Place</nuxt-link>
      </div>
      <v-spacer />
      <div class="nav-buttons">
        <v-btn type="submit" border-color="black" class="mt-4" color="#417D7A"
          ><v-icon>mdi-logout</v-icon></v-btn
        >
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "Navbar",
  methods: {},
};
</script>
<style lang="scss" scoped>
.title_navbar {
  font-size: 2.5rem;
  color: white;
}
.navbar {
  background-color: #1a3c40;
}
.nav-buttons {
  display: flex;
  margin-right: 1rem;
  position: relative;
  bottom: 9px;
}
.navbar-start {
  a {
    font-weight: bold;
    color: white;
  }
}
#white {
  color: white;
}
#header {
  align-items: center;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title {
  h1 {
    font-size: 2.5rem;
  }
}
</style>
