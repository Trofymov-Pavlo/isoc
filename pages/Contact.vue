<template> 
<div class="Shape">
    <h1 class="titre">Contacter nous</h1>
    <form class="form-contact" action="https://formsubmit.co/nathan.barrachin@gmail.com"
  method="POST">
        <input type="hidden" name="_subject" value="Nouveau message depuis Axiome">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" style="display:none">

        <input type="hidden" name="_next" value="https://tonsite.com/merci">


        <label for="name">Nom</label>
        <input type="text" id="name" name="name" required />

        <label for="email">Email</label>
        <input class="" type="email" id="email" name="email" required />

        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit" class="button">Envoyer</button>
    </form>
</div>
</template>

<script setup lang="ts">
import MainHeader from '@/components/header/mainHeader.vue';
import SubHeader from '@/components/header/subHeader.vue';

</script>

<style lang="scss" scoped> 

.titre {
    text-align: center;
    font-size: 40px;
    font-family: '', serif;
    color: #220142;
    margin-bottom: 20px;
}

.button {
    background-color: #220142;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    margin-top: 20px;
    border-radius: 4px;
}

.button:hover {
    background-color: #220142;
    transform: scale(1.05)
}
.Shape {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    border-radius: 8px;
    background-color: #ffffff;
}

.form-contact {
    display: flex;
    flex-direction: column;;
}

.form-contact textarea,
.form-contact input {
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 15px;
    border: 1px solid #000000;
    border-radius: 4px;
    font-size: 16px;
    font-family: 'arial', serif;
}

</style>