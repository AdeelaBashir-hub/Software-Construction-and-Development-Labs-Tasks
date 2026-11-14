using System;
using System.Drawing;
using System.Windows.Forms;

namespace Lab5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            this.Text = "User Login Page";
            this.Size = new Size(400, 300);
            this.StartPosition = FormStartPosition.CenterScreen;

            Label lblTitle = new Label();
            lblTitle.Text = "USER LOGIN";
            lblTitle.Font = new Font("Arial", 16, FontStyle.Bold);
            lblTitle.Location = new Point(120, 25);
            lblTitle.AutoSize = true;

            Label lblCNIC = new Label();
            lblCNIC.Text = "CNIC:";
            lblCNIC.Location = new Point(50, 90);
            lblCNIC.AutoSize = true;

            TextBox txtCNIC = new TextBox();
            txtCNIC.Location = new Point(130, 85);
            txtCNIC.Width = 180;

            Label lblPassword = new Label();
            lblPassword.Text = "Password:";
            lblPassword.Location = new Point(50, 135);
            lblPassword.AutoSize = true;

            TextBox txtPassword = new TextBox();
            txtPassword.Location = new Point(130, 130);
            txtPassword.Width = 180;
            txtPassword.PasswordChar = '*';

            Button btnLogin = new Button();
            btnLogin.Text = "Login";
            btnLogin.Location = new Point(130, 185);
            btnLogin.Width = 100;

            btnLogin.Click += (sender, e) =>
            {
                if (txtCNIC.Text == "12345-1234567-1" &&
                    txtPassword.Text == "1234")
                {
                    MessageBox.Show("Login Successful!",
                        "Information",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Information);
                }
                else
                {
                    MessageBox.Show("Invalid CNIC or Password!",
                        "Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            };

            this.Controls.Add(lblTitle);
            this.Controls.Add(lblCNIC);
            this.Controls.Add(txtCNIC);
            this.Controls.Add(lblPassword);
            this.Controls.Add(txtPassword);
            this.Controls.Add(btnLogin);
        }
    }
}
