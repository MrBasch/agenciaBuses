<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="6" md="6" class="login-card">
      <v-card class="addDialog">
        <v-card-title class="cardTitle">Login</v-card-title>
        <v-form>
          <v-text-field v-model="user" label="User"></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            @click:append="show = !show"
          ></v-text-field>
        </v-form>
        <v-card-actions class="actions-login">
          <v-spacer></v-spacer>
          <v-btn
            @click.stop="logIn((username = user), password)"
            color="#417D7A"
            >Log in</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "IndexPage",
  data() {
    return {
      user: "",
      show: "false",
      password: "",
    };
  },
  methods: {
    async logIn(username, password) {
      await fetch("http://127.0.0.1:8000/api-token-auth/", {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password }),
      }).then((res) =>
        res.json().then((data) => {
          console.log("data =", data);
          this.$auth.strategy.token.set((key = "Token"), (value = data));
        })
      );
    },
  },
};
</script>

<style scoped>
.action-login {
  flex-direction: column;
}
.addDialog {
  overflow: hidden;
  background-color: #8b8070;
}
.login-card {
  margin: auto;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  letter-spacing: 1px;
}
.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
}
.links {
  padding-top: 15px;
}
</style>
