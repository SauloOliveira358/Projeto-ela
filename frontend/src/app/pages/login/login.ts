import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [FormsModule],
  selector: 'app-login',
  styleUrl: './login.css',
  templateUrl: './login.html',
})
export class Login {
  email: string = '';
  senha: string = '';

  fazerLogin() {
    console.log('Dados preenchidos:', {
      email: this.email,
      senha: this.senha
    });
    alert(`Testando logar com o e-mail: ${this.email}`);

  }
}

