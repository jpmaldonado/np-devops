output "container_id" {
	description = "ID of container"
	value = docker_container.nginx.id
}

output "image_id" {
	description = "ID of image"
	value = docker_image.nginx.id
}

output "password" {
	description = "mdp"
	value = "12345"
	sensitive = true
}