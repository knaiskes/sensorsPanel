package main

import (
	"log"
	"net/smtp"
)

func email(msg string) {

	//credentials
	receiver := "kiriakosnaiskes@gmail.com"
	sender := "kiriakosassistant@gmail.com"
	passw := ""

	subject := "Subject: Motion detected"
	body := msg

	auth := smtp.PlainAuth(
		"",
		sender,
		passw,
		"smtp.gmail.com",
	)

	err := smtp.SendMail(
		"smtp.gmail.com:587",
		auth,
		receiver,
		[]string{receiver},
		[]byte(subject+"\r\n"+body+"\r\n"),
	)
	if err != nil {
		log.Fatal(err)
	}
}
