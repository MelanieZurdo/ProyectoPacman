import { Component, OnInit, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FirebaseService } from 'src/app/services/firebase.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.page.html',
  styleUrls: ['./forgot-password.page.scss'],
})
export class ForgotPasswordPage implements OnInit {

  form = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    });

  firebaseSvc = inject(FirebaseService);
  utilsSvc = inject(UtilsService);
  ngOnInit() {}

  /**
   * @function submit
   * @description Funcion que se ejecuta cuando el usuario selecciona la funcion de '¿Olvidaste tu contraseña?'
   * La misma realiza el envio de un mail para la restauranción.
   */
  async submit() {
    if(this.form.valid) {
      const loading = await this.utilsSvc.loading();
      await loading.present();
      this.firebaseSvc.sendRecoveryEmail(this.form.value.email).then((res) => {

        this.utilsSvc.presentToast({
          message: `Correo enviado correctamente`,
          duration: 1000,
          color: 'primary',
          position: 'bottom',
          icon: 'mail-outline'
        })

        this.utilsSvc.routerLink('auth');
        this.form.reset();

      }).catch(error => {
        console.log(error);

        this.utilsSvc.presentToast({
          message: `Correo inexistente en el sistema`,
          duration: 2000,
          color: 'primary',
          position: 'middle',
          icon: 'alert-circle-outline'
        })
      }).finally(() => {
        loading.dismiss();
      })
    }
  }
}
