resource "aws_key_pair" "vinh_key" {
    key_name = "vinh_tf_key"
    public_key = "${file("~/.ssh/id_rsa.pub")}" 
}