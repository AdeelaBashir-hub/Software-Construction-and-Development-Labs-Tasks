using System;
using System.Drawing;
using System.Windows.Forms;

namespace Lab5
{
    public class Form2 : Form
    {
        TextBox txtFirstName;
        TextBox txtLastName;
        RadioButton rbMale;
        RadioButton rbFemale;
        DateTimePicker dtpDOB;

        CheckBox chkCricket;
        CheckBox chkTV;
        CheckBox chkBooks;
        CheckBox chkMusic;
        CheckBox chkTravelling;

        Button btnSubmit;

        public Form2()
        {
            this.Text = "User Registration Form";
            this.Size = new Size(550, 650);
            this.StartPosition = FormStartPosition.CenterScreen;

            Label lblTitle = new Label();
            lblTitle.Text = "USER REGISTRATION FORM";
            lblTitle.Font = new Font("Arial", 16, FontStyle.Bold);
            lblTitle.Location = new Point(85, 20);
            lblTitle.AutoSize = true;
            this.Controls.Add(lblTitle);

            // First Name
            Label lblFirstName = new Label();
            lblFirstName.Text = "First Name *:";
            lblFirstName.Location = new Point(40, 85);
            lblFirstName.AutoSize = true;

            txtFirstName = new TextBox();
            txtFirstName.Location = new Point(180, 80);
            txtFirstName.Width = 250;

            // Last Name
            Label lblLastName = new Label();
            lblLastName.Text = "Last Name *:";
            lblLastName.Location = new Point(40, 130);
            lblLastName.AutoSize = true;

            txtLastName = new TextBox();
            txtLastName.Location = new Point(180, 125);
            txtLastName.Width = 250;

            // Gender
            Label lblGender = new Label();
            lblGender.Text = "Gender:";
            lblGender.Location = new Point(40, 175);
            lblGender.AutoSize = true;

            rbMale = new RadioButton();
            rbMale.Text = "Male";
            rbMale.Location = new Point(180, 175);
            rbMale.Checked = true;
            rbMale.AutoSize = true;

            rbFemale = new RadioButton();
            rbFemale.Text = "Female";
            rbFemale.Location = new Point(270, 175);
            rbFemale.AutoSize = true;

            // Date of Birth
            Label lblDOB = new Label();
            lblDOB.Text = "Date of Birth:";
            lblDOB.Location = new Point(40, 220);
            lblDOB.AutoSize = true;

            dtpDOB = new DateTimePicker();
            dtpDOB.Location = new Point(180, 215);
            dtpDOB.Width = 250;
            dtpDOB.MinDate = new DateTime(1950, 10, 1);
            dtpDOB.MaxDate = DateTime.Today;
            dtpDOB.Value = DateTime.Today;

            // Hobbies
            Label lblHobbies = new Label();
            lblHobbies.Text = "Select Your Hobbies:";
            lblHobbies.Location = new Point(40, 270);
            lblHobbies.AutoSize = true;
            lblHobbies.Font = new Font("Arial", 10, FontStyle.Bold);

            chkCricket = new CheckBox();
            chkCricket.Text = "Playing Cricket";
            chkCricket.Location = new Point(50, 310);
            chkCricket.AutoSize = true;

            chkTV = new CheckBox();
            chkTV.Text = "Watching TV";
            chkTV.Location = new Point(50, 345);
            chkTV.AutoSize = true;

            chkBooks = new CheckBox();
            chkBooks.Text = "Reading Books";
            chkBooks.Location = new Point(50, 380);
            chkBooks.AutoSize = true;

            chkMusic = new CheckBox();
            chkMusic.Text = "Listening Music";
            chkMusic.Location = new Point(50, 415);
            chkMusic.AutoSize = true;

            chkTravelling = new CheckBox();
            chkTravelling.Text = "Travelling to New Places";
            chkTravelling.Location = new Point(50, 450);
            chkTravelling.AutoSize = true;

            // Submit Button
            btnSubmit = new Button();
            btnSubmit.Text = "Submit";
            btnSubmit.Location = new Point(180, 510);
            btnSubmit.Width = 120;
            btnSubmit.Height = 35;

            btnSubmit.Click += (sender, e) =>
            {
                if (string.IsNullOrWhiteSpace(txtFirstName.Text) ||
                    string.IsNullOrWhiteSpace(txtLastName.Text))
                {
                    MessageBox.Show(
                        "Please enter your First Name and Last Name.",
                        "Validation Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Warning
                    );
                }
                else
                {
                    MessageBox.Show(
                        "Welcome " + txtFirstName.Text + " " + txtLastName.Text + "!",
                        "Information",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Information
                    );
                }
            };

            // Add controls to Form
            this.Controls.Add(lblFirstName);
            this.Controls.Add(txtFirstName);

            this.Controls.Add(lblLastName);
            this.Controls.Add(txtLastName);

            this.Controls.Add(lblGender);
            this.Controls.Add(rbMale);
            this.Controls.Add(rbFemale);

            this.Controls.Add(lblDOB);
            this.Controls.Add(dtpDOB);

            this.Controls.Add(lblHobbies);
            this.Controls.Add(chkCricket);
            this.Controls.Add(chkTV);
            this.Controls.Add(chkBooks);
            this.Controls.Add(chkMusic);
            this.Controls.Add(chkTravelling);

            this.Controls.Add(btnSubmit);
        }
    }
}