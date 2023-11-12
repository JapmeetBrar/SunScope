import {
  Card,
  Input,
  Textarea,
  Button,
  Typography,
} from "@material-tailwind/react";

export function Contact() {
  return (
    <div className="flex bg-gradient-to-r from-cyan-500 to-blue-500 min-h-screen justify-center py-10">
      <Card color="white" shadow={false} className="items-center p-10 h-1/2">
        <Typography variant="h4" color="blue-gray">
          Contact Us!
        </Typography>
        <Typography color="gray" className="mt-1 font-normal">
          Have a question? Type in your information below and we will reach out
          to you!
        </Typography>
        <form className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Your Name
            </Typography>
            <Input
              size="lg"
              placeholder="name"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
              crossOrigin={undefined}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Your Email
            </Typography>
            <Input
              size="lg"
              placeholder="name@mail.com"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
              crossOrigin={undefined}
            />
            <Typography variant="h6" color="blue-gray" className="-mb-3">
              Your Message or Question
            </Typography>
            <Textarea
              size="lg"
              className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
              labelProps={{
                className: "before:content-none after:content-none",
              }}
            />
          </div>
          <Button className="mt-6" fullWidth>
            send
          </Button>
        </form>
      </Card>
    </div>
  );
}
